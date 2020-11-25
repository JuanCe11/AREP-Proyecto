def merge_sort(arr):
  def merge(sub_arr,p,q):
    L = []
    R = []
    for i in range(p):
        L.append(sub_arr[i])
    for i in range(q-p):
        R.append(sub_arr[p+i])
    L.append('n')
    R.append('n')
    j=k=0
    for i in range(q):
        if L[j] < R[k] :
            sub_arr[i] = L[j]
            j += 1
        else:
            sub_arr[i] = R[k]
            k += 1
  if len(arr) > 1 :
    ls = arr[:len(arr)/2]
    rs = arr[len(arr)/2:]
    ls = merge_sort(ls)
    rs = merge_sort(rs)    
    arr = ls + rs
    merge (arr,len(arr)/2,len(arr))
  return arr

def main():
	global lista
        f = open ('info.txt','r')
        lista = f.read().split(",")
        f.close()
        print(len(lista))
        merge_sort(lista)
        print(len(lista))
main()
