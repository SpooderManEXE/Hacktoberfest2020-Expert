// function that reverse the input whether it is string or Number

const reverse = (input) => {
  const inputType = typeof input;
  input = String(input);
  let end = input.length - 1;
  let inputArr = input.split("");
  for (let i = 0; i < Math.floor(inputArr.length / 2); i++) {
    let temp = inputArr[i];
    inputArr[i] = inputArr[end];
    inputArr[end] = temp;
    end--;
  }
  input = inputArr.join("");
  return inputType === Number ? +input : input;
};
console.log(reverse("amr"));
