export const capitalizeFirstLetterOfName = (string) => {
  let new_string = " ";
  const words_arr = string.split(" ");
  words_arr.forEach((element, index) => {
    let w = element.charAt(0).toUpperCase() + element.slice(1);
    if (index === 0) {
      new_string = new_string.concat(w);
    } else if (index === words_arr.length - 1) {
      new_string = new_string.concat(" ", w);
    } else {
      new_string = new_string.concat(" ", w, " ");
    }
  });
  return new_string;
};
