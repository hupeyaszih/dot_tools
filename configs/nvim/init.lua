vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.signcolumn = "yes"
vim.opt.cursorline = true

vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartcase = true
vim.opt.ignorecase = true
vim.opt.autoread = true
vim.opt.wrap = false
vim.opt.scrolloff = 8

vim.g.mapleader = " "
vim.g.maplocalleader = " "

vim.opt.clipboard = "unnamedplus"


vim.keymap.set("i", "jk", "<ESC>")

vim.keymap.set('v', 'J', ":m '>+1<CR>gv=gv")
vim.keymap.set('v', 'K', ":m '<-2<CR>gv=gv")

vim.keymap.set('n', '<leader>cc', ':%y+<CR>', { desc = "Dosyayı kopyala" })

require("config.lazy")
