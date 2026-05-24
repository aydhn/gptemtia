import pandas as pd
from typing import Tuple, Dict, Optional
from knowledge_base.kb_config import KnowledgeBaseProfile
from knowledge_base.hybrid_retrieval import run_hybrid_retrieval
from knowledge_base.indexing import KnowledgeIndex

class ResearchQueryEngine:
    def __init__(
        self,
        documents_df: pd.DataFrame,
        chunks_df: pd.DataFrame,
        profile: KnowledgeBaseProfile,
    ):
        self.documents_df = documents_df
        self.chunks_df = chunks_df
        self.profile = profile
        self.index = KnowledgeIndex(documents_df, chunks_df)

    def query(
        self,
        query_text: str,
        top_k: Optional[int] = None,
        symbol: Optional[str] = None,
        module_name: Optional[str] = None,
        document_type: Optional[str] = None,
    ) -> Tuple[pd.DataFrame, Dict]:

        target_chunks = self.chunks_df

        if symbol:
            target_chunks = self.index.filter_by_symbol(symbol)
        if module_name and not target_chunks.empty:
            target_chunks = self.index.filter_by_module(module_name)

        if target_chunks.empty:
            return pd.DataFrame(), {"status": "success", "matches": 0, "query": query_text}

        k = top_k or self.profile.retrieval_top_k
        results_df, summary = run_hybrid_retrieval(query_text, self.documents_df, target_chunks, self.profile)

        # Apply document type filter if needed
        if document_type and not results_df.empty and 'document_type' in results_df.columns:
            results_df = results_df[results_df['document_type'] == document_type]
            summary['matches'] = len(results_df)

        return results_df.head(k), summary

    def answer_with_sources(
        self,
        query_text: str,
        top_k: Optional[int] = None,
    ) -> Tuple[str, Dict]:
        results_df, summary = self.query(query_text, top_k)

        if results_df.empty:
            return "Kanıt yetersiz. İlgili doküman bulunamadı.", summary

        answer_parts = []
        answer_parts.append(f"**Soru**: {query_text}")
        answer_parts.append("\n**Özet**: Bulunan kaynaklara göre aşağıdaki parçalar tespit edilmiştir. Ancak bu bir yatırım tavsiyesi değildir.")

        warnings = set()

        answer_parts.append("\n**Kaynaklar ve Snippets**:")
        for idx, row in results_df.iterrows():
            title = row.get('title', 'Unknown Document')
            text = row.get('text', '')
            snippet = text[:300] + "..." if len(text) > 300 else text
            score = row.get('final_score', 0.0)

            answer_parts.append(f"- **{title}** (Score: {score:.2f})")
            answer_parts.append(f"  > {snippet}")

            # Collect warnings if present
            warns = row.get('warnings', [])
            if isinstance(warns, list):
                for w in warns:
                    warnings.add(w)

        if warnings:
            answer_parts.append("\n**Uyarılar**:")
            for w in warnings:
                answer_parts.append(f"- {w}")

        answer_parts.append("\n**Sınırlamalar**: Bu sentez sadece mevcut offline dökümanlardan yapılmıştır.")
        answer_parts.append("**Disclaimer**: Bu çıktı offline knowledge base/analyst workspace çıktısıdır; gerçek emir, canlı sinyal, broker talimatı veya yatırım tavsiyesi değildir.")

        return "\n".join(answer_parts), summary

    def what_do_we_know_about_symbol(
        self,
        symbol: str,
        top_k: Optional[int] = None,
    ) -> Tuple[str, Dict]:
        query_text = f"Tüm analizler, raporlar ve kararlar {symbol} hakkında."
        return self.answer_with_sources(query_text, top_k=top_k)

    def find_warnings(
        self,
        symbol: Optional[str] = None,
        module_name: Optional[str] = None,
        top_k: int = 20,
    ) -> Tuple[pd.DataFrame, Dict]:
        query_text = "warning failed error conflict missing uncertainty"
        return self.query(query_text, top_k=top_k, symbol=symbol, module_name=module_name)
