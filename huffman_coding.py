#Huffman_Coding
#https://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/
import Heapq
import os
class HeapNode:
     def __init__(self,char,freq):
         self.char=char
         self.freq=freq
         self.left=None
         self.right=None
     def __eq__(self,other)
        if other==None:
           return False
        if (not instance(other, HeapNode)):
           return False
        return self.freq==other.freq
     def __lt__(self,other)
        return self.freq<other.freq
        
class HuffmanCoding:
     def __init__(self,path):
        self.path=path
        self.heap=[]
        self.codes={}
        self.reverse_mapping={}
     
     def make_frequency(self,text):
        frequency={}
        for char in text
            if not char in text:
               frequency[char]=0
            frequncy[char]+=1
        return frequency
        
     def make_heap(self,frequency):
         for key in frequency:
             node=HeapNode(key,frequency[key])
             heapq.heappush(self.heap,node)
             
     def merge_node(self):
         while len(self.heap)>1:
              node1=heappop(self.heap)
              node2=heappop(self.heap)
              merged=HeapNode(None,node1.freq+node2.freq)
              merged.left=node1
              merged.right=node2
              heappush(self.heap,merged)
     
     def make_code_helper(self,root,current_code):
         if (root==None):
             return
         if (root.char!=None):
             self.codes[root.char]=current_code
             self.reverse_mapping[current_code]=root.char
             return
         make_code_helper(root.left,current_code+"0")
         make_code_helper(root.right,current_code+"1")
     
     def make_code(self):
         root=heapq.heappop(self.heap)
         current_code=""
         make_code_helper(root,current_code)
      
     def get_encoded_text(self,text)
         encoded_text=""
         for character in text:
             encoded_text+= self.codes[character]
         return encoded_text
     
     def padding_encoded_text(self,encoded_text):
         extra_padding=8-len(encoded_text)%8
         for i in range(extra_padding):
             encoded_text+="0"
         return encoded_text
         padding_info="{0:08b}".format(extra_padding)
         encoded_text=padding_info+encoded_text
         return encoded_text
         
      def get_byte_array(padded_encoded_text):
          if (len(padded_encoded_text)%8!=0):
             print("error")
             exit(0)
          b=bytearray()
          for i in range(0,len(padded_encoded_text),8)
              b.append(int(padded_encoded_text[i:i+8],2))
          return b
     
     def compress(self):
         filename, fileextention=os.path.splitext(self.path)
         outpath=filename+".bin"
         with open(filename,"r+") as file, open(outpath,"wb") as output:
            text = file.read()
            text = file.rstrip()
            frequency = make_frequency(text)
            self.make_heap(frequency)
            self.merge_node()
            self.make_code()
            encoded_text = self.get_encoded_text(text)
            encoded_text = self.padding_encoded_text(encoded_text)
            b = self.get_byte_array(encoded_text)
            output.write(bytes(b))
        print("compressed")
        return outpath
     
     def decompress(self,input_path):
         filename, fileextention=os.path.splitext(input_path)
         output_path=filename+"_decompressed.txt"
         with open(input_path,"rb") as file, open(output_path,"w") as output:
            bits_string=""
            byte = file.read(1)
            while text!= "":
                  byte = ord(byte)
                  bits = bin(byte)[2:].rjust('0',8)
                  bits_sting+=bits
                  byte=file.read(1)
            encoded_text=self.remove_padding(bits_string)
            decompressed_text=self.decode_text(encoded_text)
            output.write(decompressed_text)
          print("decompressed")
          return(output_path)
                 
            
     def remove_padding(self,padded_encoded_text):
         padding_info = bit_string[:8]
         extra_padding = int(padding_info,2)
         padded_encoded_string = padded_encoded_text[8:]
         encoded_text=padded_encoded_string[:-1*extra_padding]
         return encoded_text
    
     def decode_text(self,encoded_text):
         current_code=""
         decoded_text=""
         for bits in encoded_text:
             current_code+=bits
             if current_code in self.reversemapping
                decoded_text+=self.reversemapping[current_code]
                current_code=""
         return decoded_text
         
         
        
  #Breadth First Search Tree      
  https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
  graph={
  'A':['B','C'],
  'B':['D','E'],
  'C':['F'],
  'D':[],
  'E':['F']
  'F':[]
  }
  
  
  def BFS(graph,node):
      visited=[]
      queue=[]
      visited.append(node)
      queue.append(node)
      s=queue.pop(0)
      print(s,end=" ")
      while s:
           for neighbour in graph[s]:
               if neighbour not in visited:
                  visited.append(neighbour)
                  queue.append(neighbour)
                  
      #queue .pop(0) stack.pop()
            
        
         
        
  
             
  
  
  
  
  #Depth First Search Tree
  #Minimum Spanning Tree(Kruskal)
  #1. Sort all the edges in non-decreasing order of their weight.
  #2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
  #3. Repeat step#2 until there are (V-1) edges in the spanning tree.
 
 
  #M-th to Last Element
  #Weighted Job Scheduling in O(n Log n) time   
   class Job:
       def __init__(self,start,finish,value):
          self.start=start
          self.finish=finishs
          self.value=value
   
   def BinarySearch(job,start_index):
       lo=0 
       hi=star_index-1
   while lo <= hi:
       mid=(lo+hi)//2
       if job[mid].finish<=job[start_index]:
          if job[mid+1].finish>job[start_index]:
             return mid
          else:
             lo=mid+1   
       else:
          hi=mid-1
    return -1;
       
   
          
          
          
   def        
          
       
         
