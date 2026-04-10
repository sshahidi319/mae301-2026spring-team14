import torch
from model import NanoGPT

# Hyperparameters for training
batch_size = 32
max_iters = 2000 # Adjust this to train faster or longer
eval_interval = 200
learning_rate = 1e-3
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# 1. Load the data (Make sure input.txt is in this same folder)
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Tokenization: converting characters to numbers
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

# 3. Train/Val splits
data = torch.tensor(encode(text), dtype=torch.long)
n = int(0.9*len(data))
train_data = data[:n]
val_data = data[n:]

def get_batch(split):
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - 64, (batch_size,))
    x = torch.stack([data[i:i+64] for i in ix])
    y = torch.stack([data[i+1:i+64+1] for i in ix])
    return x.to(device), y.to(device)

# 4. Initialize and train
model = NanoGPT(vocab_size).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

print(f"Starting training on {device}...")

for iter in range(max_iters):
    if iter % eval_interval == 0:
        xb, yb = get_batch('val')
        _, val_loss = model(xb, yb)
        print(f"step {iter}: val loss {val_loss.item():.4f}")
    
    xb, yb = get_batch('train')
    logits, loss = model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

print(f"Final training loss: {loss.item():.4f}")

# 5. Save the trained model for your MVP later
torch.save(model.state_dict(), 'model_ckpt.pt')
