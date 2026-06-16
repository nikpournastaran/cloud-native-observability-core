package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	// ۱. ساختن یک نمونه از سرور Gin (بدون لاگ‌های اضافی برای سرعت بیشتر)
	r := gin.Default()

	// ۲. تعریف مسیر اصلی (GET /)
	r.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"status":  "success",
			"message": "سلام! این اولین API من با زبان فوق‌العاده سریع Go هست!",
		})
	})

	// ۳. تعریف مسیر آیتم‌ها با متغیر (GET /items/:item_id)
	r.GET("/items/:item_id", func(c *gin.Context) {
		itemID := c.Param("item_id")
		c.JSON(http.StatusOK, gin.H{
			"item_id":  itemID,
			"category": "cloud-tools-go",
		})
	})

	// ۴. اجرای سرور روی پورت ۸۰۸۰ (چون پورت ۸۰۰۰ دست پایتون است)
	r.Run(":8080")
}