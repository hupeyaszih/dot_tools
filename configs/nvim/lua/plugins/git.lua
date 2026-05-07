return {
  {
    "lewis6991/gitsigns.nvim",
    config = function()
      require("gitsigns").setup({
        on_attach = function(bufnr)
          local gitsigns = require('gitsigns')

          local function map(mode, l, r, opts)
            opts = opts or {}
            opts.buffer = bufnr
            vim.keymap.set(mode, l, r, opts)
          end

          map('n', ']c', function()
            if vim.wo.diff then return ']c' end
            vim.schedule(function() gitsigns.next_hunk() end)
            return '<Ignore>'
          end, {expr=true, desc = "Sonraki Değişiklik"})

          map('n', '[c', function()
            if vim.wo.diff then return '[c' end
            vim.schedule(function() gitsigns.prev_hunk() end)
            return '<Ignore>'
          end, {expr=true, desc = "Önceki Değişiklik"})

          map('n', '<leader>hp', gitsigns.preview_hunk, { desc = "Değişikliği Önizle" })
          map('n', '<leader>hb', function() gitsigns.blame_line{full=true} end, { desc = "Satır Kimin? (Blame)" })
          map('n', '<leader>hd', gitsigns.diffthis, { desc = "Diff Ekranını Aç (Split)" })
          map('n', '<leader>hD', function() gitsigns.diffthis('~') end, { desc = "Dosya Diff (Tam Dosya)" })
          
          map('n', '<leader>hr', gitsigns.reset_hunk, { desc = "Değişikliği Sıfırla (Hunk)" })
          map('n', '<leader>hR', gitsigns.reset_buffer, { desc = "Tüm Dosyayı Sıfırla" })
        end
      })
    end,
  },
}
