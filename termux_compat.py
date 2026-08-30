# Termux compatibility helpers
try:
    import cgi
except ImportError:
    try:
        import legacy_cgi as cgi
    except ImportError:
        cgi = None
