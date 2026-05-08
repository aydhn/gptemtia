for file in commodity_fx_signal_bot/ml/*.py; do
    echo "--- $file ---"
    cat "$file" | grep "import"
done
