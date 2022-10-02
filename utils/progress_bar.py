from colorama import Fore, init; init()
from utils.ctxt import ctxt

def progress_bar(percent:float, text:str="", bar_len:int=30):
    SYMBOL = "━"
    percent_done = round(percent*100,2)
    done_len = round(percent*bar_len)
    left_len = bar_len - done_len

    print(f"   {ctxt(SYMBOL*done_len,Fore.GREEN)}{SYMBOL*left_len} {f'[{percent_done}%]'.ljust(8)} {ctxt(text,Fore.MAGENTA)}", end='\r')
    if percent == 1: print("✅")