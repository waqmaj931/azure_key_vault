from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

# Define the Key Vault URL
key_vault_url = "<add key vault URL>"


client_id = "<add client id from azure>"
tenant_id = "<add tenant id from azure>"
client_secret = "<add client secret from azure>"

# Initialize the credential and client
credential = ClientSecretCredential(tenant_id, client_id, client_secret)
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Function to get a secret from the Key Vault
def get_secret(secret_name):
    try:
        # Retrieve the secret
        secret = client.get_secret(secret_name)
        return secret.value
    except Exception as e:
        print(f"Error retrieving secret {secret_name}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    secret_name = "<secret name from azure key vault>"
    secret_value = get_secret(secret_name)
    if secret_value:
        print(f"Secret Value: {secret_value}")
    else:
        print(f"Failed to retrieve the secret: {secret_name}")
