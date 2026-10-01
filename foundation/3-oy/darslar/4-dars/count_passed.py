
def count_passed(*scores):
    count = 0
    
    for ball in scores:
        if ball >= 60:
            count+=1
    return count

print(count_passed(60, 32, 43, 94, 43))