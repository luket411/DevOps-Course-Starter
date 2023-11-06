import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


keyVaultName = "Luket411TodoAppKeyvault"
KVUri = f"https://Luket411TodoAppKeyvault.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = "testFromPython"
secretValue = "testValFromPython"

print(f"Creating a secret in Luket411TodoAppKeyvault called '{secretName}' with the value '{secretValue}' ...")

client.set_secret(secretName, secretValue)

print(" done.")

print(f"Retrieving your secret from Luket411TodoAppKeyvault.")

retrieved_secret = client.get_secret(secretName)

print(f"Your secret is '{retrieved_secret.value}'.")
print(f"Deleting your secret from Luket411TodoAppKeyvault ...")

poller = client.begin_delete_secret(secretName)
deleted_secret = poller.result()

print(" done.")
