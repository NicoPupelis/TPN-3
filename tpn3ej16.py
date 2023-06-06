import queue

cola = queue.PriorityQueue()

cola.put((1, "Doc 1 - E"))
cola.put((1, "Doc 2 - E"))
cola.put((1, "Doc 3 - E"))

primer_doc = cola.get()
print("Primer documento:", primer_doc[1])

cola.put((2, "Doc 1 - TI"))
cola.put((2, "Doc 2 - TI"))

cola.put((3, "Doc 1 - G"))

doc_1 = cola.get()
doc_2 = cola.get()
print("Documento 1:", doc_1[1])
print("Documento 2:", doc_2[1])

cola.put((1, "Doc 4 - E"))
cola.put((1, "Doc 5 - E"))
cola.put((3, "Doc 2 - G"))

print("Documentos en cola:")
while not cola.empty():
    doc = cola.get()
    print(doc[1])
