.PHONY: codegen
codegen:
	poetry run fastapi-codegen -i openapi.yml -t templates/fastapi -o src/social_links_service/codegen
