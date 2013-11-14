class AddIdQuantityToKeyPools < ActiveRecord::Migration
  def up
    add_column :key_pools, :quantity, :integer, :default => 0
  end

  def down
    remove_column :key_pools, :quantity
  end
end
