def time_conversion(s):
    if s[-2:]=="PM":
        return f"{str(int(s[:2])+12)+s[2:-2]}" if s[:2]!="12" else s[:-2]
    else: 
        return s[:-2] if s[:2]!="12" else f"00{s[2:-2]}"