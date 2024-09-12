terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "4.1.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
  subscription_id = "bfb6a9d9-68c7-4b38-ab4e-0b8066f72a58"
  features {
    subscription {
      prevent_cancellation_on_destroy = false
    }
  }
}

resource "azurerm_resource_group" "example" {
  name     = "my-terraform-rg"
  location = "West US"
}

resource "azurerm_storage_account" "example" {
  name                     = "mystorageaccount232"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  tags = {
    environment = "staging"
  }
}