return {
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    event = { "BufReadPost", "BufNewFile" },
    config = function()
      local status, treesitter = pcall(require, "nvim-treesitter.configs")
      if not status then
        return
      end

      treesitter.setup({
        ensure_installed = { "lua", "python", "javascript", "typescript", "vim", "vimdoc" },
        highlight = {
          enable = true,
          additional_vim_regex_highlighting = false,
        },
        indent = { enable = true },
      })
    end,
  },
}
