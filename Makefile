build:
	docker build -t api .

deploy:
	docker build -t api .
	docker compose up -d