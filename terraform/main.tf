# ۱. ساخت یک گروه منبع (Resource Group) در منطقه غرب اروپا (ایتالیا/آلمان)
resource "azurerm_resource_group" "rg" {
  name     = "rg-cloud-native-boilerplate"
  location = "westeurope"
}

# ۲. ساخت یک سرویس پلن (مشخصات سخت‌افزاری سرور ابری - نسخه رایگان/ارزان)
resource "azurerm_service_plan" "plan" {
  name                = "plan-cloud-native"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "F1" # نسخه رایگان آژور
}

# ۳. ساخت یک سرویس ابری برای میزبانی کانتینر داکر ما
resource "azurerm_linux_web_app" "app" {
  name                = "webapp-cloud-native-nikpour" # این اسم باید در کل دنیا یکتا باشد
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id

  site_config {
    # تنظیم سرور برای اجرای مستقیم کانتینر داکر پایتون یا Go ما
    app_command_line = ""
  }
}