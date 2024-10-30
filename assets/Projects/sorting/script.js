const arrayContainer = document.getElementById("arrayContainer");
const sortButton = document.getElementById("sortButton");
const generateButton = document.getElementById("generateButton");
const algorithmSelect = document.getElementById("algorithm");

let array = [];
const arraySize = 30;
const delay = 100;

generateArray();

// Event listeners
sortButton.addEventListener("click", () => {
  const algorithm = algorithmSelect.value;
  if (algorithm === "bubbleSort") bubbleSort();
  else if (algorithm === "selectionSort") selectionSort();
  else if (algorithm === "insertionSort") insertionSort();
  else if (algorithm === "mergeSort") mergeSort(0, array.length - 1);
  else if (algorithm === "quickSort") quickSort(0, array.length - 1);
});

generateButton.addEventListener("click", generateArray);

function generateArray() {
  array = Array.from({ length: arraySize }, () => Math.floor(Math.random() * 100) + 1);
  displayArray();
}

function displayArray() {
  arrayContainer.innerHTML = "";
  const barWidth = Math.floor(arrayContainer.offsetWidth / arraySize);
  
  array.forEach((value) => {
    const bar = document.createElement("div");
    bar.style.height = `${value * 3}px`;
    bar.style.width = `${barWidth}px`;
    bar.classList.add("bar");
    arrayContainer.appendChild(bar);
  });
}

async function bubbleSort() {
  for (let i = 0; i < array.length - 1; i++) {
    for (let j = 0; j < array.length - i - 1; j++) {
      const bars = document.getElementsByClassName("bar");
      bars[j].classList.add("active");
      bars[j + 1].classList.add("active");

      if (array[j] > array[j + 1]) {
        [array[j], array[j + 1]] = [array[j + 1], array[j]];
        displayArray();
        await delayExecution();
      }
      
      bars[j].classList.remove("active");
      bars[j + 1].classList.remove("active");
    }
  }
}

async function selectionSort() {
  for (let i = 0; i < array.length; i++) {
    let minIndex = i;
    for (let j = i + 1; j < array.length; j++) {
      const bars = document.getElementsByClassName("bar");
      bars[j].classList.add("active");
      
      if (array[j] < array[minIndex]) {
        minIndex = j;
      }
      
      bars[j].classList.remove("active");
    }
    
    if (minIndex !== i) {
      [array[i], array[minIndex]] = [array[minIndex], array[i]];
      displayArray();
      await delayExecution();
    }
  }
}

async function insertionSort() {
  for (let i = 1; i < array.length; i++) {
    let key = array[i];
    let j = i - 1;
    while (j >= 0 && array[j] > key) {
      array[j + 1] = array[j];
      j = j - 1;
      displayArray();
      await delayExecution();
    }
    array[j + 1] = key;
    displayArray();
    await delayExecution();
  }
}

async function mergeSort(left, right) {
  if (left < right) {
    const mid = Math.floor((left + right) / 2);
    await mergeSort(left, mid);
    await mergeSort(mid + 1, right);
    await merge(left, mid, right);
  }
}

async function merge(left, mid, right) {
  let leftArray = array.slice(left, mid + 1);
  let rightArray = array.slice(mid + 1, right + 1);

  let i = 0, j = 0, k = left;

  while (i < leftArray.length && j < rightArray.length) {
    if (leftArray[i] <= rightArray[j]) {
      array[k] = leftArray[i];
      i++;
    } else {
      array[k] = rightArray[j];
      j++;
    }
    displayArray();
    await delayExecution();
    k++;
  }

  while (i < leftArray.length) {
    array[k] = leftArray[i];
    i++;
    k++;
    displayArray();
    await delayExecution();
  }

  while (j < rightArray.length) {
    array[k] = rightArray[j];
    j++;
    k++;
    displayArray();
    await delayExecution();
  }
}

async function quickSort(low, high) {
  if (low < high) {
    let pivotIndex = await partition(low, high);
    await quickSort(low, pivotIndex - 1);
    await quickSort(pivotIndex + 1, high);
  }
}

async function partition(low, high) {
  let pivot = array[high];
  let i = low - 1;
  for (let j = low; j < high; j++) {
    if (array[j] < pivot) {
      i++;
      [array[i], array[j]] = [array[j], array[i]];
      displayArray();
      await delayExecution();
    }
  }
  [array[i + 1], array[high]] = [array[high], array[i + 1]];
  displayArray();
  await delayExecution();
  return i + 1;
}

function delayExecution() {
  return new Promise((resolve) => setTimeout(resolve, delay));
}
