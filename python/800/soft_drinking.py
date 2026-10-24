import sys
input = sys.stdin.readline

# n - friends
# k - bottles
# l - volume of one bottle
# c - limes
# p - grams of salt


# for a cocktail for one person:
# nl (ml of drink) + np (grams of salt) + d (slice of lime)



def solve():
    n, k, l, c, d, p, nl, np = map(int, input().split())
    drink_at_all = k * l  # in ml
    limes_at_all = c * d  # in slices

    cocktail_ml_at_all = drink_at_all // nl
    cocktail_gr_at_all = p // np

    result = min(cocktail_gr_at_all, cocktail_ml_at_all, limes_at_all) // n
    print(result)
        


    
        
if __name__ == "__main__":
    solve()