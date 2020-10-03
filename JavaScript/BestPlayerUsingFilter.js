function filterPlayer(members, rank){
  return members.filter(mem=> mem.rank < rank)
}

filterPlayer([{name: 'kohli', rank:1}, {name:'Rajesh', rank : 12}, {name: 'Dravid', rank: 5}], 10);
