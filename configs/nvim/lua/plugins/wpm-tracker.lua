return {
    {
        "leonardcser/wpm-tracker.nvim",
        config = function()
            require("wpm-tracker").setup({
                -- Log file location (CSV format)
                log_file = vim.fn.stdpath("data") .. "/wpm-tracker.csv",
                -- Rolling average window size
                average_window = 10,
                -- Minimum session length to record (milliseconds)
                min_session_length = 5000,
                -- Update interval for lualine (milliseconds)
                update_interval = 1000,
                -- Stop tracking after inactivity (milliseconds)
                idle_timeout = 5000,
            })

            -- Optional keymaps
            vim.keymap.set("n", "<leader>ws", "<cmd>WPMStats<cr>", { desc = "Show WPM statistics" })
            vim.keymap.set("n", "<leader>wl", "<cmd>WPMLog<cr>", { desc = "Open WPM log file" })
            vim.keymap.set("n", "<leader>wc", "<cmd>WPMClear<cr>", { desc = "Clear WPM history" })
            vim.keymap.set("n", "<leader>wp", "<cmd>WPMPlot<cr>", { desc = "Plot WPM data" })
        end,
    },
}
