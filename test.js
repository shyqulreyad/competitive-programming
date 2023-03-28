

// let nums = [0,0,1,1,1,1,2,3,3]

// var rm=function(nums){
//     let j=0
// for(let i=0;i<nums.length;i++){
//     if(nums[i]!==nums[i+2]){
//         nums[j]=nums[i]
//         j++
//     }
// }
// return nums

// }
// rm(nums)
// console.log(nums)
// function isMatch(s, p) {
//     const n = s.length;
//     const m = p.length;
//     const dp = Array(n + 1).fill().map(() => Array(m + 1).fill(false));
  
//     // an empty string matches an empty pattern
//     dp[0][0] = true;
  
//     // a non-empty string cannot match an empty pattern
//     for (let i = 1; i <= n; i++) {
//       dp[i][0] = false;
//     }
  
//     // check if the pattern matches an empty string or a string of '*' characters
//     for (let j = 1; j <= m; j++) {
//       if (p[j - 1] === '*' && dp[0][j - 2]) {
//         dp[0][j] = true;
//       } else if (p[j - 1] === '*') {
//         dp[0][j] = dp[0][j - 2];
//       } else {
//         dp[0][j] = false;
//       }
//     }
  
//     // check if the string matches the pattern
//     for (let i = 1; i <= n; i++) {
//       for (let j = 1; j <= m; j++) {
//         if (s[i - 1] === p[j - 1] || p[j - 1] === '.') {
//           dp[i][j] = dp[i - 1][j - 1];
//         } else if (p[j - 1] === '*') {
//           dp[i][j] = dp[i][j - 2];
//           if (s[i - 1] === p[j - 2] || p[j - 2] === '.') {
//             dp[i][j] |= dp[i - 1][j];
//           }
//         } else {
//           dp[i][j] = false;
//         }
//       }
//     }
  
//     return dp[n][m];
//   }
// const s = "aab";
// const p = "c*a*b";
// const isMatching = isMatch(s, p);
// console.log(isMatching); // true
