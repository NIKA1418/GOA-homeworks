function manualAbs(value) {
  if (typeof value !== 'number') {
    throw new TypeError('Please provide a numeric value');
  }

  return value < 0 ? -value : value;
}