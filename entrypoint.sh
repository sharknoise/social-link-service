#!/bin/sh
python -m src.social_links_service.db.create_tables
python src/__main__.py $@
