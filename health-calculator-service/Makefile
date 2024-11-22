IMAGE_NAME=health-calculator-service
PORT=5000

.PHONY: init run test build clean

init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running the Flask app in Docker..."
	docker run -p $(PORT):5000 $(IMAGE_NAME)

test:
	@echo "Running tests inside Docker..."
	docker run --rm $(IMAGE_NAME) python -m unittest discover

build:
	@echo "Building the Docker image..."
	docker build --no-cache -t $(IMAGE_NAME) .

clean:
	@echo "Cleaning up Docker containers and images..."
	docker system prune -f
