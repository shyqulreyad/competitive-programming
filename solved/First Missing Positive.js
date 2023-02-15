nums = [1,2,0]
nums.sort((x,y)=>x-y)
let a=1
for(let i=0;i<nums.length;i++){
    if((nums[i]>0)&&a==nums[i]){
        a++
    }
}
return a