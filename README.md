NC-NFT

As we know the standard ERC20  wallet address consist of 40 hexidecimals after 0x, giving us 2^160 different addresses. The idea 
of this project is the following. 

For each wallet address there is a unique picture consisting of Crosses and Noughts combinations at the standarf 3x3 field, where the
crosses and noughts are coloured some way. 

To do such a CN picture generation, I constucted an injection from the set of all hexideciamals of length 40 that is indeed a bit string
of the length 160 with a CN combinations. I did it the following way: for each of 9 cell I identify 1 bit with X or O, and 15 bits with 
RGB colors (5 for Red, ...). For 9 cells there are (2^16)^9 = 2^144 outcomes and for the last 2^16 outcomes I do the unique color of the
frame (6 bits for Red, 5 for Green, 5 for Blue). Such I indeed have an injective mapping: {ERC20 addresses} -->> {Crosses & Noughts coloured pics)
