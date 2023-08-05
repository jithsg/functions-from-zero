# functions-from-zero
[![Python application test with Github Actions](https://github.com/jithsg/functions-from-zero/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/jithsg/functions-from-zero/actions/workflows/main.yml)

### To call a microservice
''' bash
curl -X 'POST' \
  'http://127.0.0.1:8080/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "microsoft"
}'
'''