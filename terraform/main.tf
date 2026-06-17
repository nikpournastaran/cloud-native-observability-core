resource "azurerm_resource_group" "rg" {
  name     = "rg-cloud-native-boilerplate"
  location = "westeurope"
}

resource "azurerm_service_plan" "plan" {
  name                = "plan-cloud-native"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "F1" 
}

resource "azurerm_linux_web_app" "app" {
  name                = "webapp-cloud-native-nikpour" 
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id

  site_config {
    app_command_line = ""
  }
}