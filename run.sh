pip install -r requirements.txt

if [ $? -ne 0 ]; then
	echo
	echo "ERRO"
	exit 0
fi

python src/start.py
