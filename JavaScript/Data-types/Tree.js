class TreeNode {
    constructor(value) {
        this.value = value;
        this.children = [];
        this.parent = null;
    }

    addChild(child) {
        child.parent = this;
        this.children.push(child);
    }
}

/**
 * Example usage:
 * 
 * let tree = TreeNode("sakis");
 * tree.addChild(new TreeNode("george"));
 * tree.addChild(new TreeNode("george"));
 * tree.addChild(new TreeNode("george"));
 * 
 * console.log(tree);
 */