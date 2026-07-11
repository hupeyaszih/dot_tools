return {
  {
    "nvim-telescope/telescope.nvim",
    branch = "0.1.x", 
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      local telescope = require("telescope")
      
      telescope.setup({
        defaults = {
          preview = {
            treesitter = false,
          },
        },
      })

      local builtin = require("telescope.builtin")
      vim.keymap.set("n", "<leader>ff", builtin.find_files, {})
      vim.keymap.set("n", "<leader>fg", builtin.live_grep, {})
      vim.keymap.set("n", "<leader>fb", builtin.buffers, {})

      vim.keymap.set('n', 'gr', function()
          require('telescope.builtin').lsp_references({
              include_declaration = false,
              show_line = false,
              layout_strategy = "vertical",
              jump_type = "never",
          })
      end, { desc = 'Tüm proje referanslarını gör' })

      vim.keymap.set('n', 'gR', function()
          require('telescope.builtin').live_grep({
              grep_open_files = false,
              prompt_title = "Proje Genelinde Ara",
          })
      end, { desc = 'Tüm projeyi Grep ile tara' })

    end,
  },
}
