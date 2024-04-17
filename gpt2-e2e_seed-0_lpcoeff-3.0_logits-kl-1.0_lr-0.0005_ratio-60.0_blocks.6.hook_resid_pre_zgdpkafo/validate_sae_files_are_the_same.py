# pip install safetensors huggingface_hub
from safetensors import safe_open
from sparsify.loader import load_pretrained_saes
from sparsify.models.sparsifiers import SAE
import torch

tensors = {}
with safe_open("sae_weights.safetensors", framework="pt", device=0) as f:
    print(f.keys())
    for k in f.keys():
        tensors[k] = f.get_tensor(k) # loads the full tensor given a key

sae = torch.load("samples_400000.pt")
print(sae.keys())

assert torch.allclose(sae['blocks-6-hook_resid_pre.encoder.0.bias'], tensors['b_enc'])
assert torch.allclose(sae['blocks-6-hook_resid_pre.decoder.bias'], tensors['b_dec'])
assert torch.allclose(sae['blocks-6-hook_resid_pre.encoder.0.weight'], tensors['W_enc'].T)
assert torch.allclose(sae['blocks-6-hook_resid_pre.decoder.weight'], tensors['W_dec'].T)
print("All tensors matched")