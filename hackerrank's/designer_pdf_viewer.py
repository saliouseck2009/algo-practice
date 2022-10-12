def designerPdfViewer(h, word):
    return max([h[ord(i)-ord('a')] for i in word])*len(word)



def designer_pdf_viewer(h, word):
    liste = []
    for i in word:
        liste.append(h[ord(i)-ord('a')])
    return max(liste)*len(word)