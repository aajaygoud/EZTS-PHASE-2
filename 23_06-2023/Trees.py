#DICTIONARY (FOREST OF TREES)
Families={
    'ajay':
        {'sons':{'a','b','c','d','e','f'},
         'daugthers':{'g','h','i','j','k'}},
    'Natraj':
        { 'sons':{'a','b','c','d','e','f'},
          'daugther': {'g', 'h', 'i', 'j', 'k'} },
    'Praneeth':
        { 'sons':{'abcd','bcdef','cdefg','defgh','efghi','fghijk'},
          'daugthe': {'ghijkl', 'hijklm', 'imnop', 'just', 'king'} }
}
for i,j in Families.items():
    print(f"{i} has {len(j)} kids(s): ")
    print(f"{' , and '.join([str(child) for child in[*j]])}") 