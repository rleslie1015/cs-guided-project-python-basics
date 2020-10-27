function sortByLen(lst: string[]): string[] {
    return lst.sort((a, b) => a.length - b.length );
}

console.log(sortByLen(["apple", "pie", "shortcake"]))