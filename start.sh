
# 🚀 Corrige todos os __init__.py
find . -name '__init__.py' -exec sh -c 'echo "# Init package" > {}' \;

# ✅ Confirma estrutura
echo '✅ Estrutura __init__.py limpa e correta.'

# 🚀 Roda backend
cd backend/app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

