# ۱. استفاده از ایمیج رسمی Go برای کامپایل کردن کد
FROM golang:1.26-alpine AS builder
WORKDIR /app

# ۲. کپی کردن فایل‌های مدیریت وابستگی
COPY go.mod go.sum ./
RUN go mod download

# ۳. کپی کردن کدها و ساخت فایل اجرایی (Binary)
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

# ۴. استفاده از یک ایمیج فوق‌العاده سبک و خالی برای اجرای نهایی (ترفند حرفه‌ای)
FROM alpine:latest  
WORKDIR /root/
COPY --from=builder /app/main .

EXPOSE 8080

CMD ["./main"]