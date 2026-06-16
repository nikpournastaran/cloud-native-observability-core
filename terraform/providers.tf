# ۱. تعیین اینکه به کدام سرویس ابری نیاز داریم
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

# ۲. پیکربندی پرووایدر آژور
provider "azurerm" {
  features {}
}