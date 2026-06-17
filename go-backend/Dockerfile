# 1. Use the official Golang alpine image for compiling
FROM golang:1.26-alpine AS builder

WORKDIR /app

# 2. Copy all files directly (including the local module cache initialized by go mod tidy)
COPY . .

# 3. Build the binary statically without fetching external dependencies online
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

# 4. Use a lightweight alpine image for final execution
FROM alpine:latest  
WORKDIR /root/
COPY --from=builder /app/main .

EXPOSE 8080

CMD ["./main"]