import os
from huggingface_hub import create_inference_endpoint
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
MODEL_REPO_ID = os.getenv("MODEL_REPO_ID", "gpt2")
ENDPOINT_NAME = os.getenv("ENDPOINT_NAME", "vb-csharp-translator-endpoint")

if not HUGGINGFACE_TOKEN:
    print("❌ HUGGINGFACE_TOKEN not set in environment.")
    exit(1)

try:
    endpoint = create_inference_endpoint(
        ENDPOINT_NAME,
        repository=MODEL_REPO_ID,
        framework="pytorch",
        task="text-generation",
        accelerator="cpu",
        vendor="aws",
        region="us-east-1",
        type="protected",
        instance_size="x2",
        instance_type="intel-icl",
        token=HUGGINGFACE_TOKEN
    )
    print(f"✅ Endpoint created: {endpoint}")
except Exception as e:
    print(f"❌ Failed to create endpoint: {e}")