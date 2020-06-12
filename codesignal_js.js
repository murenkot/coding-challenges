/// practice 
/* 
function firstDuplicate(a) {
    if (Array.isArray(a)) {
        var dup = -1;
        let dupIndex = a.length;

        for (let i = 0; i < a.length; i++) {
            if (i >= dupIndex) {
                break;
            };
            let number = a[i];
            console.log(`current number is ${number}`);
            for (let y = i+1; y < dupIndex; y++) {
                if (i >= dupIndex) {
                    break;
                };
                console.log(a[i]);
                console.log(a[y]);
                console.log(`dupIndex: ${dupIndex}`);
                console.log("-----------");

                if (a[y] === number && (y < dupIndex || dup === -1)) {
                    console.log(true);
                    dup = a[y];
                    dupIndex = y;
                    console.log(`dup: ${dup}, dupIndex: ${dupIndex}`);
                }
            }
        }

        return dup;
    } else {
        console.log(`Input should be an array only, not ${typeof a}`);
    }
} */

function lowestDuplicate(arr) {

    for (let i = 0; i < arr.length; i++) {
        console.log(arr)
      const val = Math.abs(arr[i]);
      if (arr[val - 1] < 0) return val;
      arr[val - 1] = -arr[val - 1];
    }
    return -1;
  }

let x = [2, 1, 3, 5, 3, 2];
// x = "s";

// console.log(lowestDuplicate(x));



/* function firstNotRepeatingCharacter(s) {
    sList = s.split('');
    let sUniqueFirst = '_';
    for (let i = 0; i < s.length; i++) {
        let char = sList[i];
        let sListExtracted = [...sList];
        sListExtracted.splice(i, 1);
        
        console.log(sList);
        console.log(sListExtracted);
        if (sListExtracted.includes(char) == false){
            sUniqueFirst = char;
            break;
        }
    }
    
    return sUniqueFirst;
    
} */


function firstNotRepeatingCharacter(s) {
    sList = s.split('');
    count = {};
    for (let i = 0; i < s.length; i++) {
        let char = sList[i];
        if(count[char] === undefined) {
            count[char] = 1;
        } else {
            count[char] += 1;
        }
    }
        let uniqueList = []
      Object.keys(count).forEach(key => {
          if (count[key] ===1) {
            uniqueList.push(key);
          }
      });
      if (uniqueList.length > 0) {
          return uniqueList[0];
      } else {
        return '_';
      }
}


let stringX = "abacabad";
// console.log(firstNotRepeatingCharacter(stringX));



function rotateImage(a) {
    let len = a.length;
    for (let x = 0; x < len/2; x++) {

        for (let y = x; y < (len - x - 1); y ++) {

            let temp = a[x][y];

            a[x][y] = a[len-1-y][x];
            a[len-1-y][x] = a[len-1-x][len-1-y];
            a[len-1-x][len-1-y] = a[y][len-1-x];
            a[y][len-1-x] = temp;

        };
    };

    return a;
}

let a = [[1,2,3], 
        [4,5,6], 
        [7,8,9]];
        
// console.log(rotateImage(a));


function sudoku2(grid) {

    // check each row
    for (let i = 0; i < grid.length; i++) {
        let row = grid[i];
        let numberSet = [];
        for (let y = 0; y < grid.length; y++) {
            
        }


        if ( (new Set(row)).size !== row.length) {
            continue
        } 
    }
   


    // check each column


    // check each square 



};


let grid = 
    [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
    ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
    ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
    ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
    ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
    ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
    ['.', '.', '.', '5', '.', '.', '.', '7', '.']];


console.log(sudoku2(grid))