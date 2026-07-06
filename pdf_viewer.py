def designerPdfViewer(h, word):
    tallest = 0
    for letter in word:
        index = ord(letter) - ord('a')
        tallest = max(tallest, h[index])
    
    return tallest * len(word)

if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    print(result)
   