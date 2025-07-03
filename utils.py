import hashlib

def hash_password(password: str) -> str:
    """Hash password menggunakan SHA-256 tanpa salt (default)"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password: str, hashed: str) -> bool:
    """Memverifikasi password dengan hash"""
    return hash_password(password) == hashed
