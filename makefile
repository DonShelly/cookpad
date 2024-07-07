.PHONY: copy-vim-config

remove-cache:
	find . -type d -name "__pycache__" -exec rm -r {} +

deploy-dev:
	make refresh-venv
	make remove-cache
	. venv/bin/activate && zappa deploy dev
update-dev:
	make refresh-venv
	make remove-cache
	. venv/bin/activate && zappa update dev
update-prod:
	make refresh-venv
	make remove-cache
	. venv/bin/activate && zappa update prod

tail:
	venv/bin/zappa tail dev --since 5m

refresh-venv:
	rm -rf venv
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

copy-vim-config:
	@if [ -f ~/.vimrc ] && [ -n "${IMAGE}" ]; then \
		echo "Copying .vimrc to container ${IMAGE}..."; \
		docker cp ~/.vimrc ${IMAGE}:/root/.vimrc; \
		echo "Installing python-lsp-server[all] in container ${IMAGE}..."; \
		docker exec ${IMAGE} /bin/sh -c "pip install 'python-lsp-server[all]'"; \
	elif [ ! -f ~/.vimrc ]; then \
		echo "~/.vimrc does not exist, skipping copy."; \
	elif [ -z "${IMAGE}" ]; then \
		echo "CONTAINER variable is not set, skipping operations."; \
	fi
	@if [ -d ~/.vim ] && [ -n "${IMAGE}" ]; then \
		echo "Copying .vim directory to container ${IMAGE}..."; \
		docker cp ~/.vim ${IMAGE}:/root/.vim; \
		echo "Installing python-lsp-server[all] in container ${IMAGE}..."; \
		docker exec ${IMAGE} /bin/sh -c "pip install 'python-lsp-server[all]'"; \
	elif [ ! -d ~/.vim ]; then \
		echo "~/.vim directory does not exist, skipping copy."; \
	elif [ -z "${IMAGE}" ]; then \
		echo "CONTAINER variable is not set, skipping operations."; \
	fi

docker:
	docker-compose -f docker-compose-dev.yml up -d --build
	docker exec -it ${IMAGE} /bin/sh -c "apt update && apt upgrade -y && apt install -y awscli vim make nodejs bash && aws configure set aws_access_key_id \"${ACCESS_KEY_ID}\" && aws configure set aws_secret_access_key \"${SECRET_ACCESS_KEY}\" && aws configure set region \"${REGION}\" && aws configure set output text && aws configure set aws_session_token \"${SESSION_TOKEN}\""
	docker exec ${IMAGE} /bin/sh -c "git config --global user.email '$(shell git config --global user.email)'"
	docker exec ${IMAGE} /bin/sh -c "git config --global user.name '$(shell git config --global user.name)'"
	make copy-vim-config

docker-run:
	make docker
	docker exec -it ${IMAGE} /bin/bash -c "flask run"

test:
	pytest -s

docker-test:
	make docker
	docker exec -it ${IMAGE} /bin/sh -c "make test"

docker-exec:
	docker exec -it ${IMAGE} /bin/bash

docker-shell:
	docker system prune --all --volumes -f
	make docker
	docker exec -it ${IMAGE} /bin/bash
