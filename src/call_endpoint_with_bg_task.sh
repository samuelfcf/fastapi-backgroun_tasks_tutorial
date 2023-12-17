#!/bin/bash

total_requests=1

for ((i=1; i<=$total_requests; i++)); do
    curl -X 'GET' \
        'http://localhost:8000/with-bg-task' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        
done

wait

echo "\n"
echo "Todas as requisições concluídas!"