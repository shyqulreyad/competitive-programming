
const EventEmitter = require('events');
const celebrate = new EventEmitter();

celebrate.on('win', () => {
    console.log('celebrate!');
    }
);
celebrate.on('win', () => {
    console.log('celebrate more!');
    }
);

process.on('exit', () => {
    console.log('exit event');
    }
);
celebrate.emit('win');


let nums = [0,0,1,1,1,1,2,3,3]

var rm=function(nums){
    let j=0
for(let i=0;i<nums.length;i++){
    if(nums[i]!==nums[i+2]){
        nums[j]=nums[i]
        j++
    }
}
return nums

}
rm(nums)



let nums = [0,0,1,1,1,1,2,3,3]

var rm=function(nums){
    let j=0
for(let i=0;i<nums.length;i++){
    if(nums[i]!==nums[i+2]){
        nums[j]=nums[i]
        j++
    }
}
return nums

}
rm(nums)

