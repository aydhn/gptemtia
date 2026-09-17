# GEMINI WORKSPACE RULES — GPTEMTİA

## 1. TEMEL VE DEĞİŞMEZ KURAL: MASTER BRANCH & HER FAZ SONU COMMIT + PUSH
Bu kural projenin en yüksek öncelikli çalışma ilkesidir. Hangi yapay zeka aracı (Antigravity, Gemini, Cursor, Windsurf, Claude Code, GitHub Copilot, Codex vb.) kullanılırsa kullanılsın ve hangi sohbette olunursa olunsun İSTİSNASIZ UYGULANACAKTIR:

1. **HER ZAMAN `master` BRANCH ÜZERİNDEN İLERLENECEKTİR:**
   - Tüm geliştirme, kodlama, test, dokümantasyon ve faz çalışmaları doğrudan `master` branch'inde yürütülür.
   - Kullanıcı açıkça talep etmedikçe yan branch, geçici branch veya feature branch açılmayacak, başka branch'e geçilmeyecektir.

2. **HER FAZ / GÖREV SONRASI ZORUNLU COMMIT + PUSH:**
   - Tamamlanan her faz, alt faz, özellik veya mantıksal geliştirme bloğunun hemen ardından:
     - Değişiklikler stage edilir: `git add .` (veya ilgili dosyalar)
     - Standart, açıklayıcı bir commit mesajı ile commit oluşturulur: `git commit -m "Phase <NO>: <Açıklama>"`
     - Doğrudan remote master'a push yapılır: `git push origin master`
   - Hiçbir faz veya görev commit ve push yapılmadan sonlandırılmış sayılmaz.

3. **YEREL VE UZAK REPO HER ZAMAN %100 SENKRON VE HİZALI OLACAKTIR:**
   - `origin/master` = `yerel master` olmak zorundadır.
   - Git durumu asla "dirty" (kirli, uncommitted/untracked kalmış) bırakılmayacaktır; daima temiz (`clean working tree`) çalışılacaktır.
   - Yeni bir faza/sohbete başlamadan önce repo durumu denetlenmeli (`git status`, `git pull origin master`), yerel ile remote hizalı olmalıdır.
   - Faz bittiğinde push doğrulanmalı ve `git status`'un tertemiz olduğu teyit edilmelidir.

---

## 2. PROJE POLİTİKASI VE ÇALIŞMA SINIRLARI
Ayrıntılar için `GLOBAL_PROJECT_POLICY.md` belgesine riayet edilecektir:
- **YASAKLAR:** Gerçek borsa/broker bağlantısı, canlı emir gönderimi, gerçek para ile işlem, canlı ortam deployment'ı, yatırım tavsiyesi, web scraping, lookahead bias.
- **İZİNLİ VE HEDEFLENEN:** Gerçek tarihsel veriyle local backtest simülasyonları, yerel paper-trading motoru (sanal bakiye/pozisyon/emir/fill/PnL), Telegram research/paper-trade sinyalleri (`PAPER BUY`, `PAPER SELL`, `PAPER EXIT`, `WATCH`, `HOLD`), yerel ML eğitimi ve çıkarımı (CPU/GPU), açıklanabilir risk ve rejim analizleri.
