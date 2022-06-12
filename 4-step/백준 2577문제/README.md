## 백준 2577 나의 풀이

```javascript
const readline = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .slice(0, -1);
```

입력을 받을 때, 마지막에 빈 배열이 들어가는 문제가 있어 `slice`함수를 사용하여 배열의 마지막 부분을 잘라내었습니다.

```javascript
let myNum = {};
const index = 10;
for (i = 0; i < index; i++) {
  myNum[i] = 0;
}
```

0부터 9까지 숫자의 갯수를 최종적으로 내보내는 것이 조건이므로 반복문으로 통해서 객체를 생성하여 `key : value`형태로 관리하였습니다.

```javascript
const a = readline.map((value) => parseInt(value));
const b = a.reduce((prev, cur) => prev * cur);
const c = b.toString().split("");
```

처음 에는 위와같은 형태로 관리하였으나, 코드의 수를 조금이나마 줄일수 있는 여지가 보여서 이를 다음과 같이 개선하였습니다.

```javascript
const inputArr = readline
  .map((value) => parseInt(value))
  .reduce((prev, cur) => prev * cur)
  .toString()
  .split("");
```

---

```javascript
inputArr.map((value) => (myNum[value] = myNum[value] + 1));
for (i = 0; i < index; i++) {
  console.log(myNum[i]);
}
```

`key : value`의 형태로 숫자를 관리하여서 숫자별로 몇개가 나왔는지 파악하기가 쉬웠습니다.

다만, 객체부분을 다시 배열로 만들어서 콘솔로 찍으려고 생각하니, 과정이 복잡해지는것 같아 반복문을 통해서 조금 더 간단한 형태로 만들었습니다.
